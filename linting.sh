EXCEPTIONS=R0801,C0411
echo "Now running pylint_runner with exceptions for $EXCEPTIONS"
pylint_runner -d $EXCEPTIONS