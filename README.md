# TP 8 : Fast Scanner Multithreadé

## Benchmark

- Temps du scan TP6 (Séquentiel) : ~8 min 22s (502s) — estimation théorique, pire cas (1005 ports, timeout 0.5s chacun)
- Temps du scan TP8 (10 Threads) : ~50s — estimation théorique (502s / 10 threads)
- Gain estimé : ~10x plus rapide avec le multithreading

> Note : ces chiffres correspondent au pire cas où chaque port atteint le timeout de 0.5s (port filtré, sans réponse). Sur `127.0.0.1` avec des ports fermés, les deux scripts répondent quasi instantanément (RST immédiat), donc le test réel local ne fait pas ressortir l'écart. Le gain réel sera mesuré plus tard sur une cible filtrée (VM Windows sur vboxnet0).
