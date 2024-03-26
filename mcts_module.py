import chess
import random
import math
import time
from board_evaluation_functions import evaluate_board

class Node:
  def __init__(self, move=None, parent=None, board=None):
    self.move = move
    self.parent = parent
    self.board = board
    self.children = []
    self.wins = 0
    self.visits = 0
    self.untried_moves = list(board.legal_moves) if board else []

  def select_child(self):
    """ Select a child node with the highest UCB1 value. """
    c = 1.41  # Exploration parameter starts at \sqrt{2} -- common for 2-player games like chess
    best_value = -float('inf')
    best_node = None
    for child in self.children:
      ucb1 = child.wins / child.visits + c * math.sqrt(math.log(self.visits) / child.visits)
      if ucb1 > best_value:
        best_value = ucb1
        best_node = child
    return best_node

  def add_child(self, move):
    """ Add a new child node for the move. """
    new_board = self.board.copy()
    new_board.push(move)
    new_node = Node(move=move, parent=self, board=new_board)
    self.children.append(new_node)
    self.untried_moves.remove(move)
    return new_node

def simulate_game_with_evaluation(node, board, scheme):
  while not board.is_game_over():
    best_move = None
    best_eval = -float('inf') if board.turn == chess.WHITE else float('inf')

    for move in board.legal_moves:
      board.push(move)
      evaluation = evaluate_board(board, scheme=scheme)
      if (board.turn == chess.WHITE and evaluation > best_eval) or \
        (board.turn == chess.BLACK and evaluation < best_eval):
          best_eval = evaluation
          best_move = move
      board.pop()

    if (board.turn == chess.WHITE and evaluation > best_eval) or \
      (board.turn == chess.BLACK and evaluation < best_eval):
      best_eval = evaluation
      best_move = move

    board.push(best_move if best_move else random.choice(list(board.legal_moves)))


def select_best_move(board, max_time=None, scheme='material_count'):
  root = Node(board=board)
  start_time = time.time()

  while 1000: # Number of simulations (adjust based on performance)
    node = root
    simulation_board = board.copy()

    # Selection - UCB1 formula
    #           - Use evaluation function for the rollout phase, if not purely random
    while node.untried_moves == [] and node.children != []:
      node = node.select_child()
      simulation_board.push(node.move)

    # Expansion - expand leaf node by adding all possible next moves as its children
    #           - Use board state to generate possible moves
    if node.untried_moves != []:
      move = random.choice(node.untried_moves)
      node = node.add_child(move)
      simulation_board.push(move)

    # Simulation - From a new node, simulate a random game and get the result
    simulate_game_with_evaluation(node, simulation_board, scheme)

    # Back Propagation - Update the node and its ancestors with the result of the simulation
    while node is not None:
      node.visits += 1
      if simulation_board.result() == '1-0':
        # Increase win count for White
        temp_node = node
        while temp_node is not None:
          if temp_node.board.turn == chess.WHITE:
            temp_node.wins += 1
          temp_node = temp_node.parent
      elif simulation_board.result() == '0-1':
          # Increase win count for Black
          temp_node = node
          while temp_node is not None:
            if temp_node.board.turn == chess.BLACK:
              temp_node.wins += 1
            temp_node = temp_node.parent
      node = node.parent
    
    # If time limit exceeded, break the loop
    if max_time is not None and (time.time() - start_time) > max_time:
      break

  return max(root.children, key=lambda c: c.visits).move