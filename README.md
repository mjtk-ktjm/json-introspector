# json-introspector
deep json introspection and comparison in python

Introspecting large JSON payloads can be painful,
especially for integration testing. Comparing two JSON strings for subtle
nested differences is time consuming and error-prone. Ultimately, automating
such deep instrospection is the way to go.

This library provides a means of introspecting a single JSON object,
or comparing two JSON objects for sameness, regardless of ordering of nested
dictionary objects.

On successful deep comparison, the main function returns (True,).
On failure, the main function returns (False,str), where string is the
stringified branch object where the two objects diverge.
