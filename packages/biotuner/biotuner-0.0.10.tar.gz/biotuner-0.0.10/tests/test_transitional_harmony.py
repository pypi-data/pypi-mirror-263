import pytest
import numpy as np
from transitional_harmony import transitional_harmony
from matplotlib.figure import Figure

# Fixture for creating a test instance of transitional_harmony
@pytest.fixture
def test_instance():
    data = np.random.rand(44100)  # Example data
    return transitional_harmony(
        sf=44100,
        data=data,
        peaks_function="EMD",
        precision=0.1,
        n_harm=10,
        max_harm_freq=150,
        harm_function="mult",
        min_freq=2,
        max_freq=80,
        n_peaks=5,
        n_trans_harm=10,
        mode="win_overlap",
        overlap=10,
        FREQ_BANDS=None
    )

# Test the initialization
def test_initialization(test_instance):
    assert test_instance.sf == 44100
    assert len(test_instance.data) == 44100
    assert test_instance.peaks_function == "EMD"
    assert test_instance.precision == 0.1
    assert test_instance.n_harm == 10
    # Continue with other attribute assertions

# Test compute_trans_harmony method
@pytest.mark.parametrize("mode, overlap, delta_lim, graph, save", [
    ('win_overlap', 10, 20, False, False),
    ('IF', 5, 30, True, False),
    # Add more combinations
])
def test_compute_trans_harmony(test_instance, mode, overlap, delta_lim, graph, save):
    trans_subharm, time_vec_final, subharm_melody = test_instance.compute_trans_harmony(
        mode=mode, 
        overlap=overlap, 
        delta_lim=delta_lim,
        graph=graph,
        save=save
    )
    assert isinstance(trans_subharm, list)
    assert isinstance(time_vec_final, list)
    assert isinstance(subharm_melody, list)
    # Validate length of lists and types of elements
    # Add additional assertions as necessary

# Test compare_deltas method
def test_compare_deltas(test_instance):
    deltas = [10, 20, 30]
    fig = test_instance.compare_deltas(deltas)
    assert isinstance(fig, Figure)
    # Add more validations as needed

# Test for invalid inputs and exception handling
def test_invalid_input():
    with pytest.raises(TypeError):  # Adjust the exception type based on your class's validation
        transitional_harmony(sf='invalid', data=np.random.rand(44100), ...)

# Test for handling of empty data
def test_empty_data():
    with pytest.raises(ValueError):  # Adjust the exception as per your class's validation
        transitional_harmony(sf=44100, data=np.array([]), ...)

# Add more tests for edge cases and other functionalities
