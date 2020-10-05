string="A donkey kong movie;; Bruce Lee is mass"

print type(string)
string=string.lower()
print type(string)
##Split

#########   just string.split() wont affect string
#########   string = string.split() ## default split("")
string = string.split()
print type(string)

##join
string = str(string)
print "JOIN:"+"".join(string)

print type(string)
##Replace
string = string.replace("my","thy")
string = string.replace(string[0:2],"th") ## Splicing, last int is not included
print string
