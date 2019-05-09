

from confound_isolating.data_simulation import simulate_confounded_data
from confound_isolating.sampling import (random_index_2remove,
                                         confound_izolating_index_2remove)

# Simulate data
X, y, z, = simulate_confounded_data(link_type='direct_link', n_samples=100,
                          n_features=100)
ids = list(range(0, y.shape[0]))

# Remove index with random or Confound Izolating methods


ratio_dens_1, index_test_remove_1, kde_y_1, kde_z_1, kde_yz_1, scale_method = \
    random_index_2remove(y, z)

ratio_dens, ratio_remove, index_test_remove, kde_y, kde_z, kde_yz = \
    confound_izolating_index_2remove(y, z)



