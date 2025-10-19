# /*
# * stack.sh
# *
# * el stack
# * uso de esa cosa
# *
# * configurar variables
# *
# * arbol1:
# *
# * variables
# *
# *  ProgramaArbol: 0x0:MiVariable1 = "foo"
# *  ProgramaArbol: 0x1:MiVariable2 = "bar"
# *  ProgramaArbol: 0x2:MiVariable3 = "hello"
# *  ProgramaArbol: 0x3:MiVariable4 = "world"
# *
# * arbol2:
# * 
# * variables
# *
# *  ProgramaArbol: 0x0:MiVariable1 = "apple"
# *  ProgramaArbol: 0x1:MiVariable2 = "banana"
# *  ProgramaArbol: 0x2:MiVariable3 = "what"
# *  ProgramaArbol: 0x3:MiVariable4 = "pear"
# *
#
#   BasOS^# src stack.sh
#   foo bar hello world.
#   apple banana what pear.
#   foo bar hello world.
#   
#   BasOS^#
#
# */

#
# arbol1
#

# primera frase
setv 0
stra foo
setv 1
stra bar
# segunda frase
setv 2
stra hello
setv 3
stra world

print 0
prtxt  
print 1
prtxt  
print 2
prtxt  
print 3
echo .

#
# arbol2
#

# begin incrementa el stack
begin

# primera frase
setv 0
stra apple
setv 1
stra banana

# segunda frase
setv 2
stra what
setv 3
stra pear

# imrpimirlos
print 0
prtxt  
print 1
prtxt  
print 2
prtxt  
print 3
echo .
# liberarlos
frst 0
frst 1
frst 2
frst 3

end

#
# arbol1 de nuevo
#

# imrpimirlos
print 0
prtxt  
print 1
prtxt  
print 2
prtxt  
print 3
echo .
# liberarlos
frst 0
frst 1
frst 2
frst 3