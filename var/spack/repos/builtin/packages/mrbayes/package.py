from spack import *


class Mrbayes(Package):
    """
MrBayes is a program for Bayesian inference and model choice across a wide range of phylogenetic and evolutionary models. MrBayes uses Markov chain Monte Carlo (MCMC) methods to estimate the posterior distribution of model parameters. 
    """
    homepage = "http://nbisweden.github.io/MrBayes/"

    version('git', branch='develop', git='https://github.com/NBISweden/MrBayes.git')

    def install(self, spec, prefix):
        config_args = []
        configure('--prefix={0}'.format(prefix), *config_args)

        make()
        make('install')

