import gen
import compression

num_epochs = 1500

# Simulate
states = gen.run(num_epochs)
# Compress using run-length encoding
comp = compression.runlength(states)

print('Raw length: ' + str(states.size))
print('Compressed length: {0} [{1}%]'.format(comp.size, 100*(comp.size / states.size)))
