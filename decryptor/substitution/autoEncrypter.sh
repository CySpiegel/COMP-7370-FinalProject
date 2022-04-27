inputs=`ls unencryptedBooks --ignore-backups`

for i in $inputs; do
    python3 simpleSubCipher.py ./unencryptedBooks/$i \
	    ./encryptedBooks/$i

    # diff ./actual_output/$i.out ./expected_output/$i.out > \
    #      ./reports//$i --ignore-space-change --ignore-case \
    #      --side-by-side --ignore-blank-lines
done