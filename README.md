# TP 8 : Fast Scanner Multithreadé

## Benchmark

- Temps du scan TP6 (Séquentiel) : ~3 min 22s après test, pire cas (plus de 10 ports, timeout 0.5s chacun)
- Temps du scan TP8 (10 Threads) : ~7s — après test (plus de 20s / 10 threads)
- Gain estimé : ~10x plus rapide avec le multithreading

> Note : Le gain réel est mesuré sur une cible filtrée (VM Windows sur min interface locale).
