cmd1="cat "
cmd2=".ts >> full.ts"
# modify '716' to the amount of .ts files in your own case
for (( i=1; i<=716; i++ ))
		do
				cmd=${cmd1}${i}${cmd2}
				eval $cmd
		done
