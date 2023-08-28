# %%
import heapq

class BeamSearchDecoder:
    def __init__(self, model, beam_width):
        self.model = model
        self.beam_width = beam_width

    def beam_search(self, initial_state, max_length):
        # Initialize the beam search
        beam = [(0.0, [initial_state])]
        
        # Perform beam search
        for _ in range(max_length):
            candidates = []
            for score, states in beam:
                # Generate the next set of candidate states
                next_states = self.model.generate_next_states(states[-1])
                for next_state, next_score in next_states:
                    candidate = (score + next_score, states + [next_state])
                    candidates.append(candidate)
            
            # Select the top candidates based on the scores
            beam = heapq.nlargest(self.beam_width, candidates, key=lambda x: x[0])
        
        # Return the best sequence
        best_score, best_sequence = beam[0]
        return best_sequence

# Example model
class ExampleModel:
    def __init__(self):
        self.transitions = {
            'A': [('B', 0.5), ('C', 0.3)],
            'B': [('D', 0.4), ('E', 0.7)],
            'C': [('D', 0.2), ('E', 0.6)],
            'D': [('F', 0.9)],
            'E': [('F', 0.8)],
            'F': [('G', 0.7)],
            'G': [('H', 1.0)]
        }

    def generate_next_states(self, state):
        return self.transitions.get(state, [])

# Initialize the model and define the beam width
model = ExampleModel()
beam_width = 3

# Initialize the beam search decoder
decoder = BeamSearchDecoder(model, beam_width)

# Perform beam search starting from the initial state for a maximum length of 5
initial_state = 'A'
max_length = 5
best_sequence = decoder.beam_search(initial_state, max_length)

# Print the best sequence
print("Best sequence:", best_sequence)
