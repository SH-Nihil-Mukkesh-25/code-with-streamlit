1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
import
streamlit
st
as
file_path
" example. txt "
def get_file_handler():
# Open the file in append mode,
open(file_path,
file
file
return
# Use the cached file handler
get_file_handler()
file handler
which creates the file if it doesn't exist
# Write to the file using the cached handler
st.button("Write to File").
if
file handler. write("New
line of text\n")
file _ handler. flush() #
Ensure the content is written immediately
st.success("Wrote a new
line to the file!