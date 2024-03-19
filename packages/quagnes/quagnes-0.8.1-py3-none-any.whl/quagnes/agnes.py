#   A module for solving Agnes solitaire
#   Copyright (C) 2019, 2024 Ray Griner (rgriner_fwd@outlook.com)
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# File:    agnes.py
# Date:    2019-03-19
# Author:  Ray Griner
# Purpose: AgnesState class definition
# Changes:
# [20240314RG]: (1) Add type hints. (2) Change attribute name _AgnesState.exp
#   to _AgnesState.exposed. (3) Make moves and _AgnesState.exposed tuples
#   instead of lists. (4) Minor bug fix when validating suits in deck passed
#   as input. (5) previous version assumed all piles in tableau were exposed,
#   now this is controlled via an input parameter. (6) Change
#   '_AgnesState.found' attribute to 'foundation' (7) Removed
#   `move_from_same_suit` parameter until I can confirm exactly what the game
#    variant rules are.
# [20240316RG]: (1) Improve documentation. (2) Add `no_print` parameter
#    to _undo_move that is set to True when called from Agnes.print_history.
#    (3) Reimplement `move_from_same_suit` parameter functionality (except now
#    renamed to `split_same_suit_runs`. To facilitate, calc_n_movable changed
#    to return list of integers with the number of cards that can be moved
#    instead of the maximum number that can be moved from a pile.
#    (4) Change `move_to_empty_pile` parameter to be 'none', 'any', 'highest'
#    instead of True (now 'any') or False (now 'none').
#    (5) Change `expose_all` parameter name to `face_up`.
#------------------------------------------------------------------------------
"""A module for solving Agnes solitaire. """

import random
import copy
from typing import Set, Optional, Union
from dataclasses import dataclass

__all__ = ['Agnes']
__author__ = 'Ray Griner'

# Each card is a tuple with two members. Use these to access.
#_RANK = 0
#_SUIT = 1

#------------------------------------------------------------------------------
# Type aliases
#------------------------------------------------------------------------------
CardRank = int
CardSuit = int
#Card = tuple[CardRank, CardSuit]
#Card = collections.namedtuple('Card', 'rank suit')
#
#class Card(NamedTuple):
#    rank: CardRank
#    suit: CardSuit

@dataclass(frozen=True)
class Card:
    """Dataclass representing a card in the deck."""
    rank: CardRank
    suit: CardSuit

    def __repr__(self) -> str:
        return f'({self.rank}, {self.suit})'

    def twochar(self) -> str:
        """Return a two character string representing the card, eg, '3♦'."""
        if self.rank==0:
            rank_str = 'A'
        elif self.rank==12:
            rank_str = 'K'
        elif self.rank==11:
            rank_str = 'Q'
        elif self.rank==10:
            rank_str = 'J'
        else:
            rank_str = str(self.rank)

        if self.suit==0:
            suit_str='♣'
        elif self.suit==1:
            suit_str='♦'
        elif self.suit==2:
            suit_str='♠'
        elif self.suit==3:
            suit_str='♥'

        return rank_str+suit_str

@dataclass(frozen=True)
class DealMove:
    """Dataclass representing a deal from the stock."""
    def __str__(self) -> str:
        return 'Deal'

@dataclass(frozen=True)
class MoveToFound:
    """Dataclass representing a move of one card to the foundation."""
    from_: int
    suit: CardSuit
    expose: bool

    def __str__(self) -> str:
        str2 = ''
        str1 = (f'Move bottom card from pile {self.from_} to foundation '
                f'{self.suit}')
        if self.expose:
            str2 = ' (exposes a card)'
        return str1 + str2

@dataclass(frozen=True)
class TablMove:
    """Dataclass representing a move in the tableau."""
    from_: int
    n_cards: int
    to_: int
    expose: bool

    def __str__(self) -> str:
        str2 = ''
        str1 = (f'Move {self.n_cards} card(s) from pile {self.from_} to pile '
               f'{self.to_}')
        if self.expose:
            str2 = ' (exposes a card)'
        return str1 + str2

AgnesGraph = dict[CardSuit, set[CardSuit]]
ExpHidd = tuple[list[Card], list[Card], list[Card], list[Card], list[Card],
    list[Card], list[Card]]
#AgnesMove = tuple[int, ...]
AgnesMove = Optional[Union[MoveToFound, TablMove, DealMove]]

#------------------------------------------------------------------------------
# Static functions
#------------------------------------------------------------------------------
# describe_move: Change a list that represents a move into text description for
#   printing
#------------------------------------------------------------------------------
def _describe_move(move: Optional[AgnesMove]) -> str:
    if move is None:
        return 'Initial layout'
    else:
        return str(move)

#------------------------------------------------------------------------------
# The largest trees hit a memory limit when writing to the losing_states set
# so here we do some simple compression for the string representation rather
# than using the form generated by __repr__ (which we keep for use in debugging
# output).
#------------------------------------------------------------------------------

# Each card is a tuple represented in the string as ASCII code 48-99
def _multtpl(tpl: Card) -> str:
    return str(chr(48+13*tpl.suit+tpl.rank))

# Each tableau pile is a string of ASCII codes representing the cards,
#  starting with '+'.
def _strpile(pile: list[Card]) -> str:
    return '+' + ''.join([_multtpl(tpl) for tpl in pile])

# Join the strings for each pile
def _strexp(exposed: ExpHidd, hidden: ExpHidd) -> str:
    retlist = []
    for pile in exposed:
        retlist.append(_strpile(pile))
    for pile in hidden:
        retlist.append(_strpile(pile))
    return '|'.join(retlist)

#------------------------------------------------------------------------------
# Depth-first search to detect if a king or a set of kings is blocking cards
#  in such a way that the game is unwinnable.
#------------------------------------------------------------------------------
def _cyclic(g: AgnesGraph) -> bool:
    current_path: set[CardSuit] = set()
    visited: set[CardSuit] = set()

    def visit(vertex: CardSuit) -> bool:
        if vertex in visited: return False
        visited.add(vertex)
        current_path.add(vertex)
        for neighbor in g.get(vertex, ()):
            if neighbor in current_path or visit(neighbor): return True
        current_path.remove(vertex)
        return False

    return any(visit(v) for v in g)

class Agnes:
    """
    A class used to represent a game of Agnes solitaire

    Attributes
    ----------
    n_states_checked : int
        Number of states examined
    n_deal : int
        Number of deals performed
    n_move_card_in_tableau : int
        Number of moves of card(s) between piles in tableau
    n_move_to_foundation : int
        Number of times a card was moved to foundation
    n_no_move_possible : int
        Number of states created where no move was possible
    max_depth : int
        Maximum depth of the search tree
    current_depth : int
        Current depth of the search tree
    max_score : int
        Maximum score obtained (i.e., maximum number of cards moved
        to the foundations). For the default input parameters, the
        program backtracks as soon as it detects a state cannot be
        won. A higher maximum score may be possible if the game were
        played in full.
    maximize_score : boolean
        Stores value of input parameter with the same name
    move_to_empty_pile : str
        Stores value of input parameter with the same name
    move_same_suit : boolean
        Stores value of input parameter with the same name
    split_same_suit_runs : boolean
        Stores value of input parameter with the same name
    face_up : boolean
        Stores value of input parameter with the same name
    maximize_score : boolean
        Stores value of input parameter with the same name
    track_threshold : boolean
        Stores value of input parameter with the same name
    print_states : bool
        Stores value of input parameter with the same name
    test_deck : bool
        Stores value of input parameter with the same name
    deck_filename : bool
        Stores value of input parameter with the same name
    max_states : boolean
        Stores value of input parameter with the same name
    """

    def __init__(self,
                 move_to_empty_pile: str = 'none',
                 move_same_suit: bool = False,
                 split_same_suit_runs: bool = True,
                 face_up: bool = False,
                 maximize_score: bool = False,
                 track_threshold: int = 0,
                 print_states: bool = False,
                 test_deck: int = 0,
                 deck_filename: Optional[str] = None,
                 max_states: int = 0):
        """
        Parameters
        ----------
        move_to_empty_pile : {'none', 'high 1', 'any 1', 'high run', 'any run'}
            Optional parameter, default is 'none'. Describes which single
            cards or runs can be moved to an empty pile.
            'none': (default), no card can be moved from the tableau. Empty
                piles are only filled when dealing from stock.
            'any 1': Any single card can be moved.
            'high 1': Any single card of highest rank can be moved. For
                example, if the base card is a 3, then a 2 can be moved.
            'any run': Any movable run can be moved.
            'high run': Any movable run that is built down from a card of
                highest rank.
        move_same_suit : boolean, optional (default = False)
            If True, only permit moving sequences of cards in the tableau
            that are the same suit. Otherwise, permit moving sequences of
            cards that are the same color.
        split_same_suit_runs : boolean, optional (default = True)
            If True, a sequence of the same suit can be split by a move.
        face_up : boolean, optional (default = False)
            Deal all cards face up in the tableau.
        track_threshold : int, optional (default = 0)
            If the number of cards left in the stock is greater than or
            equal to this value, track losing states in a single set for
            the whole game. This set can consume a lot of memory if some of
            the other options are chosen that allow a large number of moves
            (eg, `move_to_empty_pile != 'none'`).
        print_states : boolean, optional (default = False)
            Print game states as moves are made. See `Agnes.print_history`
            for output format.
        maximize_score : boolean, optional (default = False)
            Determine the maximum score. Disables the algorithm used when
            `move_to_empty_pile == 'none'` that stops playing the game
            when it detects a game is unwinnable.
        test_deck : {0, 1}, optional (default = 0)
            If 0, a random deck is generated. If 1, a fixed test deck that
            wins is used.
        deck_filename : string, optional
            Read deck from text file, If empty, a random deck will be
            used by calling random.shuffle and reversing the results.
            The text file should consist of 52 lines with each line is
            formatted as "(rank, suit)", where rank is in 0..12 and
            suit is in 0..3. Note the first card dealt is the base card.
        max_states : int, optional
            Terminate game with return code 3 when number of states
            examined exceeds this threshold.  0 (default) means no
            threshold is used.
        """
        if print_states: print('Start Agnes()')

        # Initial deck, before standardizing so the base card has rank 0
        self._initial_deck: list[Card] = []
        # Deck after standardizing the base card
        self._deck: list[Card] = []
        # List to track the valid moves remaining for each state in the stack
        self._all_valid_moves: list[list[AgnesMove]] = []
        # List of states we have been since the last deal or move-to-foundation
        # This is to check that we don't enter an infinite loop of moving
        # cards in the tableau.
        self._check_loop_states: list[set[str]] = [set()]
        # Moves performed to reach each state.
        self._moves: list[AgnesMove] = []
        self._curr_state: _AgnesState = _AgnesState()
        # States (as str) that we have already identified as losing
        self._losing_states: Set[str] = set()
        self.test_deck = test_deck
        self.n_states_checked = 1
        self.n_deal = 1
        self.n_move_card_in_tableau = 0
        self.n_move_to_foundation = 0
        self.n_no_move_possible = 0
        self._max_states = max_states
        self.deck_filename = deck_filename
        self.move_to_empty_pile = move_to_empty_pile
        self.move_same_suit = move_same_suit
        self.print_states = print_states
        self.track_threshold = track_threshold
        self.split_same_suit_runs = split_same_suit_runs
        self.max_depth = 0   # maximum depth of the search tree
        # Current depth of the search tree (i.e., number moves played to reach
        # the current state. Does not count moves played where search had to
        # backtrack.
        self.current_depth = 0
        self.face_up = face_up
        self.maximize_score = maximize_score
        self.max_score = 1   # maximum score found
        #self.move_from_same_suit = move_from_same_suit
        #move_from_same_suit : boolean, optional
        #    Allow moving a pile off of the same suit. For example,
        #    when True (default), will allow moving the three of clubs
        #    from under the four of clubs to under the four of spades in
        #    the tableau.

        if self.test_deck == 0:
            if not self.deck_filename:
                self._initialize_deck()
            else:
                self._initialize_deck_from_file(self.deck_filename)
        else:
            self._initialize_test_deck(self.test_deck)

    def __repr__(self) -> str:
        return (f'move_same_suit:{self.move_same_suit}\n'
               f'Deck:{self._deck}\nStates:\n{self._curr_state}')

    def print_history(self) -> str:
        """Print history for a won or stopped game.

        Return a string that contains the history of the game through
        the current state. Because there is currently no way to play the
        game one move at a time, the only games where the state after
        `Agnes.play` is executed that will show moves are winning games
        or games that were stopped due to `Agnes.max_states` being exceeded.

        A -1 in the foundation indicates no card has yet been played in the
        column. Tableau piles are presented horizontally instead of
        vertically as 'T0' - 'T6', where cards on the right side of the
        line can be played, and a '|' separates hidden cards and exposed
        cards in each tableau pile.

        Cards are represented as in input decks as '(rank, suit)', where
        rank is 0–12 and suit is 0–3, where suits 0 and 2 are the same
        color, as are suits 1 and 3. The normalized cards are printed, ie,
        all cards have a number subtracted from their rank so that the base
        card has rank 0.

        Returns
        -------
        A string as described above.
        """
        states: list[_AgnesState] = []
        # inefficient, since losing_states set may be quite large, but we
        # expect to only do once for each winning game
        # a copy is needed because making/undoing moves changes the
        # current state stored in the `Agnes` object.
        copyself: Agnes = copy.deepcopy(self)
        while copyself._moves:
            states.append(copy.deepcopy(copyself._curr_state))
            copyself._undo_move(no_print=True)
            copyself._curr_state.set_valid_moves(self.move_to_empty_pile,
                move_same_suit=self.move_same_suit,
                split_same_suit_runs=self.split_same_suit_runs)
        # Get the initial state also
        states.append(copy.deepcopy(copyself._curr_state))
        return str(list(reversed(states)))

    # Print the deck used in a simple text format
    def export_deck(self, filename: str) -> None:
        """Export the deck to a text file.

        Write one card per line as (rank, suit) where suit is 0, 1, 2, or 3,
        and rank is 0, 1, ..., 12. Note this this is the deck as input
        using the `deck_filename` parameter or as randomly generated
        the deck is standardized to have a base card of 0 for internal
        used. The standardized cards are displayed in the
        `Agnes.print_history` or `print_states` functions.

        Arguments
        ---------
        filename: str
            Output filename

        Returns
        -------
        None
        """
        outstr=''
        #for card in self._initial_deck:
            #outstr += '({:2d}, {:d})\n'.format( card[_RANK], card[_SUIT])
        outstr = '\n'.join([ f'({card.rank:2d}, {card.suit:d})'
                             for card in self._initial_deck])
        f = open(filename, 'w', encoding='utf-8')
        f.write(outstr)
        f.close()

    def _initialize_deck_from_file(self, filename: str) -> None:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        self._initial_deck = []
        line_number = 0
        dupset=set()
        for line in lines:
            line_number += 1
            stripped = line.rstrip()
            hasparen = stripped.startswith('(') and stripped.endswith(')')
            noparen = stripped.strip('()')
            rank, suit = noparen.split(',')
            rank = rank.strip()
            suit = suit.strip()
            # [20240314RG]: bug fix, was using 'suit.isdigit' instead of
            # 'suit.isdigit()'
            if (not hasparen or not rank.isdigit() or not suit.isdigit()
                   or int(rank)>12 or int(suit)>3):
                raise ValueError('Lines in deck_filename should be of the '
                   "form '(rank, suit)' where rank is in 0..12 and suit is "
                   f'in 0..3. Found: {stripped} (line {line_number})')
            card = Card(rank=int(rank), suit=int(suit))
            if card in dupset:
                raise ValueError('Duplicate card in deck '
                                 f'found on line {line_number}')
            else:
                dupset.add(card)
            self._initial_deck.append(card)
        if line_number != 52:
            raise ValueError('52 lines in deck_filename '
                             f'expected. Found: {line_number}')

    # Set the maximum number of cards that can be moved in a given pile.
    def _initialize_deck(self) -> None:
        self._initial_deck = []
        for rank in range(0, 13):           # Ranks: 0-12
            for suit in range(0,4):                        # Suits: 0-3
                self._initial_deck.append(Card(rank=rank, suit=suit))
        random.shuffle(self._initial_deck)
        self._initial_deck.reverse()

    #  Winning
    def _initialize_test_deck(self, test_deck: int) -> None:
        if test_deck == 1:
            win_base = [(6, 2)]
            win_row1 = [(9, 1),(5, 1),(7, 3),(5, 3),(3, 3),(9, 0),(5, 0)]
            win_row2 =        [(12,2),(2, 1),(6, 0),(4, 2),(13,3),(2, 2)]
            win_row3 =               [(8, 1),(4, 3),(7, 0),(8, 2),(3, 2)]
            win_row4 =                      [(10,0),(1, 3),(11,1),(8, 0)]
            win_row5 =                             [(13,1),(9, 3),(4, 0)]
            win_row6 =                                    [(9, 2),(1, 1)]
            win_row7 =                                           [(7, 1)]
            win_stock1 = [(6, 3),(11,2),(5, 2),(3, 0),(2, 0),(11,0),(13,0)]
            win_stock2 = [(10,3),(3, 1),(8, 3),(1, 0),(10,1),(11,3),(7, 2)]
            win_stock3 = [(12,0),(10,2),(4, 1),(12,3),(12,1),(6, 1),(13,2)]
            win_stock4 = [(1, 2),(2, 3)]
        elif test_deck != 0:
            raise ValueError('test_deck takes values 0 (default: use random '
                'deck), 1 (wins)')

        # Make a list of lists representing the deck
        temp_deck = [win_base, win_row1, win_row2, win_row3, win_row4,
                     win_row5, win_row6, win_row7, win_stock1, win_stock2,
                     win_stock3, win_stock4]

        # Flatten the list of lists
        for x in temp_deck:
            for y in x:
                self._initial_deck.append(Card(rank=y[0], suit=y[1]))

    def play(self) -> int:
        """Play the game of Agnes and return integer status.

        Parameters
        ----------
        None

        Returns
        -------
        An integer with the following meanings:
            1: Won
            2: Lost
            3: Terminated because number of states created exceeds
               max_states
        """

        first_state = self._curr_state

        # Reset the indexing of all cards so base card has rank 0
        self._deck = []
        for i in range(0, 13*4):
            self._deck.append(Card(rank=(self._initial_deck[i].rank
                                - self._initial_deck[0].rank) % 13,
                                   suit=self._initial_deck[i].suit))
        # Deal base card to foundation
        first_state.play_base_card(self._deck[0])

        # Deal next cards to Tableau
        for i in range(0,7):
            for j in range(i,7):
                first_state.deal_onto_pile(pile_index=j, deck=self._deck,
                    face_up=bool(self.face_up or j == i))

        first_state.set_valid_moves(self.move_to_empty_pile,
                                    self.move_same_suit,
                                    self.split_same_suit_runs)
        #print(first_state)
        self._all_valid_moves = [first_state.valid_moves]
        done = 0
        if self.print_states: print(first_state)
        if (self.move_to_empty_pile == 'none' and not self.maximize_score
                and first_state.any_pile_blocked()):
            return 2
        else:
            while done == 0:
                done = self._perform_move()
                if self.print_states: print(self._curr_state)
            self.current_depth = self._curr_state.depth
            return done

    def _undo_move(self, no_print: bool) -> None:
        """Undo last move (last item in `_moves` stack).

        The three-step process when executing a move is described in the
        docstring of `_perform_move`. This function reverses step (1)
        by manually resetting the attributes and step (3) (by popping the
        last items from the stack. Step (2) is not reversed as the counters
        that were updated were meant to be cumulative.

        Parameters
        ----------
        no_print : bool
            Do not print 'Undo move' to standard output, even if
            `self.print_states = True`. Without this parameter, the
            function `Agnes.print_history` would print 'Undo move' as it
            unwinds the game play to show the history of winning moves.

        Returns
        -------
        None
        """

        if self.print_states and not no_print: print('Undo move')
        new_state = self._curr_state
        curr_move = self._moves.pop()
        self._all_valid_moves.pop()
        if self.split_same_suit_runs:
            self._check_loop_states.pop()
        new_state.depth = new_state.depth - 1
        if curr_move is None:
            raise ValueError('_undo_move: curr_move should not be None')
        elif isinstance(curr_move, MoveToFound):
            # if we exposed a card when we moved the card beneath it to the
            # foundation, turn it back over before moving the card back from
            # the foundation
            if curr_move.expose:
                new_state.hidden[curr_move.from_].append(
                    new_state.exposed[curr_move.from_].pop())
            # now move the card back from the foundation
            new_state.exposed[curr_move.from_].append(
                Card(rank=new_state.foundation[curr_move.suit],
                     suit=curr_move.suit))
            new_state.foundation[curr_move.suit] -= 1
        elif isinstance(curr_move, DealMove):
            # Deal from stock
            if new_state.n_stock_left == 0:
                # Put two cards back on deck and remove them from the tableau
                new_state.n_stock_left = 2
                new_state.exposed[0].pop()
                new_state.exposed[1].pop()
            else:
                new_state.n_stock_left = new_state.n_stock_left + 7
                for pile in new_state.exposed:
                    pile.pop()
        elif isinstance(curr_move, TablMove):
            # if we exposed a card when we moved the pile, turn it back over
            # before moving the pile back
            if curr_move.expose:
                new_state.hidden[curr_move.from_].append(
                    new_state.exposed[curr_move.from_].pop())
            # now move the pile back
            for n_to_pop in range(-1*curr_move.n_cards,0):
                new_state.exposed[curr_move.from_].append(
                    new_state.exposed[curr_move.to_].pop(n_to_pop)
                    )

        if self._moves:
            new_state.curr_move = self._moves[-1]
        else:
            new_state.curr_move = None
        # [20240315RG] bug fix for printing
        new_state.valid_moves = self._all_valid_moves[-1]

    def _perform_move(self) -> int:
        """Perform a move. Call _undo_move if no possible move.

        To make a move, update:
            (1) the appropriate attributes of `self._curr_state`
                (`exposed`, `hidden`, `n_stock_left`, `foundation`)
            (2) any counters in `self` that count the various types of
                moves made (`n_move_to_foundation`,`n_deal`,
                `n_move_card_in_tableau`).
            (3) append to the three stacks that track the evolution of the
                game:` _moves`, `_all_valid_moves`, `_check_loop_states`.
                While we could have used a single stack to manage these three
                items, we intentionally do not maintain a stack of
                _AgnesState objects. This would simplify the code (eg,
                `_undo_move` could be replaced with popping the last state
                from the stack), but increases the run-time 4.75-fold
                for 1000 simulations (80m vs 381m).

        Arguments
        ---------
        None

        Returns
        -------
        Integer with the values:
           0 if there were no valid moves, but depth > 0 so _undo_move was
             called, OR there was a valid move so it was made, but it didn't
             result in a win.
           1 if game is won (there was a valid move, it was made, and the
             game was won)
           2 if game is lost (no valid moves, and depth == 0)
           3 if self.n_states_checked > self._max_states and
             self._max_states>0

        """
        self.n_states_checked += 1
        if self._curr_state.depth > self.max_depth:
            self.max_depth = self._curr_state.depth

        if self._max_states > 0 and self.n_states_checked>self._max_states:
            #print(f'Terminated at {self.n_states_checked} moves', flush=True)
            return 3

        # Check the score and whether it's greater than the max score
        valid_moves = self._all_valid_moves[-1]
        won_game = False
        any_pile_blocked = False

        # Lost the game!
        if (self._curr_state.depth == 0 and not valid_moves):
            self.n_no_move_possible += 1
            return 2
        elif not valid_moves:
            # keep track of states that we know are losers
            if self._curr_state.n_stock_left >= self.track_threshold:
                self._losing_states.add(str(self._curr_state.n_stock_left) +
                                       _strexp(self._curr_state.exposed,
                                               self._curr_state.hidden))
            self.n_no_move_possible += 1
            self._undo_move(no_print=False)
            return 0
        else:
            # Make a move
            curr_move = valid_moves.pop()
            new_state = self._curr_state
            new_state.curr_move = curr_move
            new_state.depth += 1
            if isinstance(curr_move, MoveToFound):
                last_card = new_state.exposed[curr_move.from_].pop()
                if curr_move.expose:
                    new_state.exposed[curr_move.from_].append(
                        new_state.hidden[curr_move.from_].pop())
                new_state.foundation[last_card.suit] += 1
                if self.split_same_suit_runs:
                    check_loops: set[str] = set()
                self.n_move_to_foundation += 1
                # +4 here because -1 represents no card in pile
                score = sum(new_state.foundation)+4
                if score > self.max_score:
                    self.max_score = score
                if score == 52: won_game = True
            elif isinstance(curr_move, DealMove):
                # Deal from stock
                if new_state.n_stock_left == 2:
                    new_state.deal_onto_pile(0, self._deck, True)
                    new_state.deal_onto_pile(1, self._deck, True)
                else:
                    for pile_index in range(0,7):
                        new_state.deal_onto_pile(pile_index, self._deck, True)
                if self.split_same_suit_runs:
                    check_loops = set()
                # If move_to_empty_pile == 'none', then our trick of speeding
                # up run-time by seeing if any lower cards are blocked by
                # the highest card won't work, because the highest card
                # could be moved to an empty pile
                if (self.move_to_empty_pile == 'none'
                        and not self.maximize_score):
                    any_pile_blocked = new_state.any_pile_blocked()
                self.n_deal += 1
            elif isinstance(curr_move, TablMove):
                self.n_move_card_in_tableau += 1
                for n_to_pop in range(-1*curr_move.n_cards,0):
                    new_state.exposed[curr_move.to_].append(
                        new_state.exposed[curr_move.from_].pop(n_to_pop)
                        )
                if curr_move.expose:
                    new_state.exposed[curr_move.from_].append(
                        new_state.hidden[curr_move.from_].pop())
                if self.split_same_suit_runs:
                    check_loops = copy.copy(self._check_loop_states[-1])
            else:
                raise TypeError(f'curr_move is {curr_move}')
            #------------------------------------------------------------------
            # It's possible we've already evaluated that this state is losing.
            # Consider the case where there are two possible independent moves
            # (M1: Move 1 card from Pile 1 to 2, M2: move 1 card from pile 5
            # to 6). Once you check that M1->M2 doesn't win, no need to check
            # M2->M1
            #------------------------------------------------------------------
            if (self._curr_state.n_stock_left >= self.track_threshold
                and (str(new_state.n_stock_left)
                + _strexp(new_state.exposed, new_state.hidden))
                    in self._losing_states):
                new_state.valid_moves = []
                if self.print_states:
                    print('Already checked the new state, '
                          'so setting valid_moves to empty')
            elif (self.move_to_empty_pile == 'none' and any_pile_blocked):
                if self.print_states:
                    print('New state is a block, '
                          'so setting valid_moves to empty')
                new_state.valid_moves = []
            elif (self.split_same_suit_runs and _strexp(new_state.exposed,
                          new_state.hidden) in check_loops):
                if self.print_states:
                    print('New state is a loop, '
                          'so setting valid_moves to empty')
                new_state.valid_moves = []
            else:
                new_state.set_valid_moves(self.move_to_empty_pile,
                          move_same_suit=self.move_same_suit,
                          split_same_suit_runs=self.split_same_suit_runs)

            if self.split_same_suit_runs:
                check_loops.add(_strexp(new_state.exposed, new_state.hidden))

            if won_game:
                self._moves.append(curr_move)
                # [RG20240316]
                if self.split_same_suit_runs:
                    self._check_loop_states.append(set())
                self._all_valid_moves.append([])
                return 1
            elif not new_state.valid_moves:
                if new_state.n_stock_left >= self.track_threshold:
                    self._losing_states.add(str(new_state.n_stock_left)
                                       + _strexp(new_state.exposed,
                                                 new_state.hidden))
                self._all_valid_moves.append([])
                if self.split_same_suit_runs:
                    self._check_loop_states.append(set())
                self._moves.append(curr_move)
            else:
                self._all_valid_moves.append(new_state.valid_moves)
                if self.split_same_suit_runs:
                    self._check_loop_states.append(check_loops)
                self._moves.append(curr_move)

            return 0

#------------------------------------------------------------------------------
# AgnesState class - represents a state in the game.
#------------------------------------------------------------------------------
class _AgnesState:
    """Represent a state in the game.

    Attributes:
    -----------
    depth : int
        The number of moves played to reach the state.
    n_stock_left : int
        Number of cards remaining in the stock.
    exposed : tuple(list[Card])  (7-tuple)
        A 7-tuple where each item represent the exposed cards showing in
        each of the 7 piles of the tableau.
    hidden : tuple(list[Card])  (7-tuple)
        A 7-tuple where each item represent the hidden cards in each of the
        7 piles of the tableau.
    found : list[int]
        List of size four representing the top card in each of the four
        foundations. A value of -1 indicates no card in the foundation.
    n_movable : list[int]
        List of size seven representing the number of cards that can be
        moved from each of the 7 columns in the tableau (without
        considering whether there is a destination that columns can be
        moved to).  For example, if the bottom cards in a column are the
        Three of Spades, the Four of Spades, and the 5 of Hearts, the
        value is 2, even if there is no Five of Clubs or Spades exposed.
    curr_move : list[int]
        Last move played to reach this state
    valid_moves : list[AgnesMove]
        List of valid moves for this state. It is initialized when the state
        is created and then moves are popped off as they are tried.
    force_move : list[AgnesMove]
        List of move that will be forced. This will override the list of
        valid moves. For example, moving a card from the tableau to an
        empty foundation pile may be forced. See `set_valid_states`
        for details.
    """
    # default constructor
    def __init__(self) -> None:
        self.depth = 0
        self.n_stock_left = 52
        # Exposed and hidden cards in tableau.
        self.exposed: ExpHidd = ([], [], [], [], [], [], [])
        self.hidden: ExpHidd = ([], [], [], [], [], [], [])
        self.foundation = [-1, -1, -1, -1]
        self.curr_move: Optional[AgnesMove] = None
        self.valid_moves: list[Optional[AgnesMove]] = []
        self.force_move: list[Optional[AgnesMove]] = []

    # String representation of object (print() will use this)
    #def vertstr(self) -> str:
    #    str1 = (f'\nMove: {_describe_move(self.curr_move)}\n\n'
    #        f'depth:{self.depth}, n_stock_left:{self.n_stock_left}, '
    #        f'valid_moves:{self.valid_moves}\n')
    #
    #    foundlist=[]
    #    for i, value in self.foundation:
    #        if value == -1:
    #            foundlist.append('  ')
    #        else
    #            foundlist.append(Card(rank=value, suit=suit).twochar())
    #    str2 = 'Foundations:' + ' '.join(foundlist)

    def __repr__(self) -> str:
        return (f'\nMove: {_describe_move(self.curr_move)}\n\n'
            f'depth:{self.depth}, n_stock_left:{self.n_stock_left}, '
            f'valid_moves:{self.valid_moves}\nFoundations:{self.foundation}\n'
            f'T0:{self.hidden[0]} | {self.exposed[0]}\n'
            f'T1:{self.hidden[1]} | {self.exposed[1]}\n'
            f'T2:{self.hidden[2]} | {self.exposed[2]}\n'
            f'T3:{self.hidden[3]} | {self.exposed[3]}\n'
            f'T4:{self.hidden[4]} | {self.exposed[4]}\n'
            f'T5:{self.hidden[5]} | {self.exposed[5]}\n'
            f'T6:{self.hidden[6]} | {self.exposed[6]}\n'
            )

    # Uncomment to print format similar to, but not identical to v0.6 (ie,
    # format of moves is different. For use when `Agnes.face_up` is True.
    #
    #def __repr__(self) -> str:
    #    return (f'\nMove: {_describe_move(self.curr_move)}\n\n'
    #        f'depth:{self.depth}, n_stock_left:{self.n_stock_left}, '
    #        f'valid_moves:{self.valid_moves}\nFoundations:{self.foundation}\n'
    #        f'T0:{self.exposed[0]}\nT1:{self.exposed[1]}\n'
    #        f'T2:{self.exposed[2]}\nT3:{self.exposed[3]}\n'
    #        f'T4:{self.exposed[4]}\nT5:{self.exposed[5]}\n'
    #        f'T6:{self.exposed[6]}\n')

    def calc_n_movable(self, pile_index: int, move_same_suit: bool,
                       split_same_suit_runs: bool) -> list[int]:
        """Return list of number of cards that can be moved from a pile.

        Note this just checks the number of cards from the bottom of the
        pile than can be moved according to the rules. It does not check
        whether there is somewhere the selected set of cards can be moved
        to. The latter is done in `set_valid_moves`.

        Arguments
        ---------
        pile_index : int
            Index of the pile to check
        move_same_suit : bool
            If True, a card sequence must be the same suit to be moved.
            Otherwise, a card sequence must be the same color to be moved.
        split_same_suit_runs : bool
            If True, a sequence of the same suit can be split by a move.

        Returns
        -------
        List of integers with number of cards that can be moved from a
        pile.
        """
        pile = self.exposed[pile_index]
        ret_list = []
        if pile:
            for card_index, card in enumerate(reversed(pile)):
                try:
                    #above_card = pile[card_index + 1]
                    above_card = pile[-1 - card_index - 1]
                except IndexError:
                    above_card = None

                # Check rank & check suit is same color (convention is
                # suits (0,2) and (1,3) are the same color)
                if not card.rank - card_index == pile[-1].rank:
                    break

                if not (card.suit == pile[-1].suit
                    or (not move_same_suit
                        and (card.suit % 2) == (pile[-1].suit % 2))):
                    break

                if (split_same_suit_runs or above_card is None
                        or not (above_card.rank == card.rank + 1
                            and above_card.suit == card.suit)):
                    ret_list.append(card_index + 1)
        return ret_list

  # Deal a single card from stock onto the pile identified by pile_index
    def deal_onto_pile(self, pile_index: int, deck: list[Card],
                       face_up: bool) -> None:
        """Deal one card from the stock onto the pile identified by pile_index.
        """
        if face_up:
            self.exposed[pile_index].append(deck[52 - self.n_stock_left])
        else:
            self.hidden[pile_index].append(deck[52 - self.n_stock_left])
        self.n_stock_left = self.n_stock_left - 1

    def any_pile_blocked(self) -> bool:
        """Check if game is unwinnable after a deal.

        This should only be called if `Agnes.move_to_empty_pile=='none'`.
        Otherwise, the game might be winnable even though suits are
        blocked because the 'kings' can be moved to an empty pile to
        unblock the cards beneath them.

        Creates a graph indicating whether a given 'king' is covering in
        a pile a lower rank card of the same suit or a king of another
        suit. If the graph has a cycle, the game cannot be won.

        Returns
        -------
        bool that is True if any pile or combination of piles blocks a win.
        """
        graph: AgnesGraph = {0: set(), 1: set(), 2: set(), 3: set()}
        for i, exp_pile in enumerate(self.exposed):
            pile = self.hidden[i] + exp_pile
            if pile:
                # Check for blocks
                king_found = [False, False, False, False]
                for current_card in reversed(pile):
                    if current_card.rank == 12:
                        king_found[current_card.suit] = True
                    for k in range(0, 4):    # loop over suits
                        if (king_found[k]
                                    and (current_card.rank < 12
                                         or current_card.suit != k)):
                            graph[k].add(current_card.suit)
        return _cyclic(graph)

    # Set self.validmoves with the three types of moves
    def set_valid_moves(self, move_to_empty_pile: str,
                        move_same_suit: bool,
                        split_same_suit_runs: bool) -> None:
        """Set self.valid_moves to the valid moves available.

        Three types: DealMove()
                     TablMove(from_=, to_=, n_cards=, expose=)
                     MoveToFound(from_=, suit=, expose=)

        If it is possible to put a card in the foundation, and that card
        is less than or equal to two ranks higher than the highest card
        in the foundation of the other suit, then moving the card to
        the foundation is forced, ie, it is the only move stored in
        `set.valid_moves`. (If multiple piles have a card meeting this
        criteria, then the move from the last pile is forced.)

        For example, suppose the base card is an Ace and the 6 of Spades
        is the highest spade in the foundation. Then if there is a valid
        move to put any club from Ace to 8 in the foundation, that move
        will be forced (ie, the only valid move stored). If there is a
        valid move to put the 9 of Clubs in the foundation, this would be
        stored as a valid move, but would not be forced, because the 9
        of clubs might be needed as a target to move the 8 of Spades under.

        Parameters
        ----------
        move_same_suit : bool
            If True, a card sequence must be the same suit to be moved.
            Otherwise, a card sequence must be the same color to be moved.
        split_same_suit_runs : bool
            If True, a sequence of the same suit can be split by a move.

        Returns
        -------
        None
        """
        self.valid_moves = []
        self.force_move = []

        # Deal (DealMove dataclass)
        if self.n_stock_left > 0:
            self.valid_moves.append(DealMove())

        for pile_index, exp_pile in enumerate(self.exposed):
            # Moves in tableau (TablMove dataclass)
            #
            # Get a list of the number of cards that are movable
            # according to the input parameters. This does not yet consider
            # if there is a location the cards can be moved to.
            n_movable = self.calc_n_movable(pile_index, move_same_suit,
                                            split_same_suit_runs)

            for n_to_move in n_movable:
                # 'Source' card: the one we want to move
                src_card = exp_pile[-n_to_move]
                if n_to_move == len(exp_pile):
                    expose = bool(self.hidden[pile_index])
                else:
                    expose = False

                # 'target' pile is the pile we are trying to move to
                for target_index in range(0,7):
                    if target_index == pile_index: continue
                    if not self.exposed[target_index]:
                        if ( ((move_to_empty_pile == 'any 1' or
                             (move_to_empty_pile == 'high 1'
                              and src_card.rank == 12)) and n_to_move == 1) or
                             ((move_to_empty_pile == 'any run' or
                             (move_to_empty_pile == 'high run'
                              and src_card.rank == 12)))):
                            self.valid_moves.append(TablMove(
                                from_=pile_index, n_cards=n_to_move,
                                to_=target_index, expose=expose))
                        else:
                            continue
                    else:
                        target_card = self.exposed[target_index][-1]

                        if (src_card.rank == target_card.rank - 1
                            and ((src_card.suit
                                  - target_card.suit) % 2 == 0)):
                            self.valid_moves.append(TablMove(
                                from_=pile_index, n_cards=n_to_move,
                                to_=target_index, expose=expose))

            if exp_pile:
                # Move card to foundation (MoveToFound dataclass)
                last_card = exp_pile[-1]
                expose = bool(len(exp_pile) == 1 and self.hidden[pile_index])
                if last_card.rank - 1 == self.foundation[last_card.suit]:
                    self.valid_moves.append(MoveToFound(from_=pile_index,
                            suit=last_card.suit, expose = expose))
                    same_color_suit = (last_card.suit + 2) % 4

                    # See discussion in docstring about forcing moves
                    if last_card.rank <= self.foundation[same_color_suit]+2:
                        self.force_move = [MoveToFound(from_=pile_index,
                                suit=last_card.suit, expose=expose)]

        if self.force_move:
            self.valid_moves = self.force_move

    def play_base_card(self, base_card: Card) -> None:
        """Play the base card into the foundation.

        Arguments
        ---------
        base_card : Card

        Returns
        -------
        None
        """
        self.foundation[base_card.suit] = 0
        self.n_stock_left = self.n_stock_left - 1
