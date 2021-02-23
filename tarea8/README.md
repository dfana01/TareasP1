# tarea8

## Autor
- <Dante Fana Badia>20156079@ce.pucmm.edu.do

## Soluciones 

### Método maestro

```
t(n) = t(n/2) + O(1)
a = 1
b = 2 
f(n) = O(1)

    f(n) = n^log2(1) = 1 ∴ aplica el caso 2.
    t(n) = O(1 log n) = O(log n)
```

### Sustitución

Asumimos complejidad O(log n) ∴ t(n) <= log n 
```
t(n) = t(n/2) + O(1)
    <= log n/2 + 1
    = log n / 2 + 1
    = log n + log 2 + 1 (eliminamos los valores mas pequeño y nos quedamos con el asintotico)
    <= log n
```

### Arbol

```
t(n) = t(n/2) + O(1)

#node   tree         cost 
 1       1            1
 1       n/2^2        1
 1       n/2^3        1
 1       n/2^4        1
 
base case => t(n/2^i)
1 = n/2^i => log2(n) = i

Σ[i=0...log2(n)] i = log2(n) + 1 
```


