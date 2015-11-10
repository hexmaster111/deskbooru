# deskbooru
upcoming project written in python that allows a booru-style tagging system to organize and provide search for local images as well as searching, viewing, and bulk downloading of various booru websites

#Todo
Plans for scripts

tagging.py - tagging system to assign tags to various files and store in a primitive database
------------
CURRENT priority:
input a file
hash the file and assign the hash to a filename in a database
assign IDs to the hashes by inserting into database
input tags for said file
assign tags to IDs in the database
write IDs under tags in the tagfile

HIGH priority:
bulk file tagging (e.g. tag all files in a folder, tag all files passed to the script)
tag assignment "fixing" - rehash all files in a folder to reassign hashes to new filenames

MEDIUM priority:
input tags to be removed or added to already-tagged file
assigning favorite/rating (e.g. safe, questionable, explicit) to images
different tag types (e.g. artist, series/IP, character, general)
-----------

search.py
-----------
CURRENT priority:
input tags for a search
read tagfile
query tagfile for all IDs that match the tags
return all filenames that match the tags

HIGH priority:
search regex (e.g. wildcard, all files matching [tag] but not [tag], all files matching [tag] or [tag])

MEDIUM priority:
less important search regex (e.g. favorites only, rating) (kind of goes with favorites/rating)
