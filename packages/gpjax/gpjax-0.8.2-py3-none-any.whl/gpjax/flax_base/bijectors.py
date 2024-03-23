from gpjax.flax_base.types import BijectorLookupType, DomainType
import tensorflow_probability.substrates.jax.bijectors as tfb
import typing as tp

Bijectors: BijectorLookupType = {
    "real": tfb.Identity(),
    "positive": tfb.Softplus(),
}
