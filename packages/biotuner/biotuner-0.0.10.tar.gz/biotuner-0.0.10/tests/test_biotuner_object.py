import pytest
from biotuner.biotuner_object import compute_biotuner  # Adjust this import based on your actual module structure
import numpy as np
# Define a list or a generator function that provides test cases
# Here, we're directly defining test cases for simplicity
test_cases = [
    # Test default initialization
    {
        "args": {"sf": 1000},
        "expected": {
            "sf": 1000,
            "peaks_function": "EMD",
            "precision": 0.1,
            "compute_sub_ratios": False,
            "n_harm": 10,
            "harm_function": "mult",
            "extension_method": "consonant_harmonic_fit",
            "ratios_n_harms": 5,
            "ratios_harms": False,
            "ratios_inc": True,
            "ratios_inc_fit": False,
            "scale_cons_limit": 0.1,
        },
    },
    # Test custom initialization
    {
        "args": {
            "sf": 2048,
            "data": [1, 2, 3],
            "peaks_function": "FOOOF",
            "precision": 0.05,
            "compute_sub_ratios": True,
            "n_harm": 5,
            "harm_function": "div",
            "extension_method": "all_harmonic_fit",
            "ratios_n_harms": 3,
            "ratios_harms": True,
            "ratios_inc": False,
            "ratios_inc_fit": True,
            "scale_cons_limit": 0.2,
        },
        "expected": {
            "sf": 2048,
            "data": [1, 2, 3],
            "peaks_function": "FOOOF",
            "precision": 0.05,
            "compute_sub_ratios": True,
            "n_harm": 5,
            "harm_function": "div",
            "extension_method": "all_harmonic_fit",
            "ratios_n_harms": 3,
            "ratios_harms": True,
            "ratios_inc": False,
            "ratios_inc_fit": True,
            "scale_cons_limit": 0.2,
        },
    },
]

@pytest.mark.parametrize("case", test_cases)
def test_compute_biotuner_init(case):
    # Unpack the test case
    args = case["args"]
    expected = case["expected"]
    
    # Initialize the object
    obj = compute_biotuner(**args)
    
    # Assert each expected property
    for prop, expected_value in expected.items():
        assert getattr(obj, prop) == expected_value, f"Expected {prop} to be {expected_value}, got {getattr(obj, prop)}"

# Sample data for testing
sine_wave = np.sin(np.linspace(0, 2 * np.pi, 1000))
random_data = np.random.rand(1000)

test_cases = [
    (sine_wave, "EMD_fast", None, 0.1, 1000, 1, 60, 2, False),
    (random_data, "EMD_fast", None, 0.1, 1000, 1, 60, 2, False),
    # Add more test cases as needed
]

@pytest.mark.parametrize("data, peaks_function, FREQ_BANDS, precision, sf, min_freq, max_freq, min_harms, compute_sub_ratios", test_cases)
def test_peaks_extraction(data, peaks_function, FREQ_BANDS, precision, sf, min_freq, max_freq, min_harms, compute_sub_ratios):
    biotuner = compute_biotuner(sf=sf)
    biotuner.peaks_extraction(data=data, peaks_function=peaks_function, FREQ_BANDS=FREQ_BANDS, precision=precision, sf=sf, min_freq=min_freq, max_freq=max_freq, min_harms=min_harms, compute_sub_ratios=compute_sub_ratios)
    
    # Verify output types and values as needed, for example (array for peaks):
    assert isinstance(biotuner.peaks, np.ndarray), "Expected peaks to be a numpy array"
    assert all(isinstance(peak, float) for peak in biotuner.peaks), "Expected peaks list to contain floats"
    # Add more assertions to validate the output based on the input conditions

# Example of an edge case test
def test_peaks_extraction_with_empty_data():
    biotuner = compute_biotuner(sf=1000)
    with pytest.raises(ValueError):  # Assuming your method raises a ValueError for empty data
        biotuner.peaks_extraction(data=np.array([]))