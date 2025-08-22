def calcular_imc(peso, altura):

    try:
        peso = float(peso)
        altura = float(altura)
        """Calcula el Índice de Masa Corporal (IMC) dado el peso en kg y la altura en metros."""
        if altura <= 0 or peso <= 0:
            raise ValueError("La altura y el peso deben ser mayores que cero.")
        imc = peso / (altura ** 2)
        return imc
    except ValueError:
        raise ValueError("El peso y la altura deben ser números válidos.")
