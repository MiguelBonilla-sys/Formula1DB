from Extract.Formula1Extract import Formula1Extract

# Crear extractor y cargar datos limpios
extractor = Formula1Extract("qualifying_results.csv")

# Cargar y limpiar datos automáticamente
extractor.queries()
extractor.clean_data(strategy='fill_mean')

# Mostrar datos 
print(extractor.response())
