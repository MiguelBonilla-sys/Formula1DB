from Extract.Formula1Extract import Formula1Extract

extractor = Formula1Extract("qualifying_results.csv")

extractor.queries()

print(extractor.response())
