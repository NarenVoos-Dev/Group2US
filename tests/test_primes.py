import pytest
from primes import es_primo, listar_primos_hasta


def test_es_primo_small():
    assert es_primo(2) is True
    assert es_primo(3) is True
    assert es_primo(4) is False
    assert es_primo(17) is True
    assert es_primo(18) is False


def test_es_primo_edges():
    assert es_primo(0) is False
    assert es_primo(1) is False
    assert es_primo(-5) is False
    # non-int should return False
    assert es_primo(4.5) is False


def test_listar_primos_hasta():
    assert listar_primos_hasta(1) == []
    assert listar_primos_hasta(2) == [2]
    assert listar_primos_hasta(10) == [2, 3, 5, 7]
    assert listar_primos_hasta(20) == [2, 3, 5, 7, 11, 13, 17, 19]
