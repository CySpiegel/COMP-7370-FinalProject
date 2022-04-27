inputs=`ls encryptedBooks --ignore-backups`

for i in $inputs; do
    echo "Decrypting: " $i
    python3 betterSubCrack.py ./encryptedBooks/$i \
	    ./decryptedBooks/$i

    # diff ./actual_output/$i.out ./expected_output/$i.out > \
    #      ./reports//$i --ignore-space-change --ignore-case \
    #      --side-by-side --ignore-blank-lines
done