shows=[
"Avatar: the last airbendr",
"Archur",
"Ben 10",
" spongepop",
"jimi",
"narges mirzaei"
]

def  main():
    cleaned_shows=[]
    for show in shows:
        cleaned_shows.append(show.strip().title())
        print(','.join(cleaned_shows))
main()