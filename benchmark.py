from benchmark.plotting import GraphVisualization
from src.kifli import *


def benchmark_generation_pochon():
    n = 150     #Nombre de répétition
    taille_pochon = 100

    obj = GraphVisualization("Génération de pochon")
    obj.measure_execution_time(n, gen_pochon, taille_pochon)
    obj.plot_data(["green"], ["gen_pochon()"])


def benchmark_gen_cle_privee():
    n = 100     #Nombre de répétition
    taille_pochon = 100

    obj = GraphVisualization("Génération clé privée")
    obj.measure_execution_time(n, gen_cle_privee, taille_pochon)
    obj.plot_data(["green"], ["gen_cle_privee()"])


def benchmark_gen_cle_publique():
    n = 150     #Nombre de répétition
    taille_pochon = 100
    cle_privee = gen_cle_privee(taille_pochon)

    obj = GraphVisualization("Génération clé publique")
    obj.measure_execution_time(n, gen_cle_publique, cle_privee)
    obj.plot_data(["green"], ["gen_cle_publique()"])



if __name__ == "__main__":
    benchmark_generation_pochon()
    benchmark_gen_cle_privee()
    benchmark_gen_cle_publique()