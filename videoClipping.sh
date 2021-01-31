offset=0.2
delimiter=$1
delim=`echo $delimiter - $offset | bc`
echo "delimiter is $1"
file="$2"
# echo "$file"
ffmpeg -i $file -af silencedetect=n=-50dB:d=1.8 -f null - 2> vol.txt
python3 ./startEndScript.py $file
FILE=./temp.txt

x=0
while [ ! -f "$FILE" ]; 
do
    if x==0
    then
        x=1
    fi 

done
exec 5<startEnd.txt
exec 4<videoName.txt
n=1
line1=""
line2=""
while read line1<&5 && read line2<&5 && read fileName<&4
do
# reading each line
echo "$line1--------$line2"
n=$((n+1))
ffmpeg -i $file -ss ${line1} -to ${line2} -strict -2 -async 1 ${fileName}
echo "completed $n"
done

exec 5<&-
echo "helloWorld2"
rm ./temp.txt