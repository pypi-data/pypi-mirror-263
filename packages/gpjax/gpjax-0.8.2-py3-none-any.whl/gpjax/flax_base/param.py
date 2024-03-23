import jax.numpy as jnp
import typing as tp
from flax.experimental import nnx
from gpjax.flax_base.types import DomainType, A


class AbstractParameter(nnx.Variable[A]):
    domain: DomainType = "real"
    static: bool = False

    def __init__(self, value: A, *args, **kwargs):
        super().__init__(jnp.asarray(value), *args, **kwargs)


class PositiveParameter(AbstractParameter[A]):
    domain: DomainType = "positive"
