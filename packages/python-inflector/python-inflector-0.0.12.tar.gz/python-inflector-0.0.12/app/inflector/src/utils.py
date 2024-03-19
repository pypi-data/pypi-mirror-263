__author__ = 'omrio'

import unicodedata


def unicodify(st):
    '''
    Convert the given string to normalized Unicode (i.e. combining characters such as accents are combined)
    If given arg is not a string, it's returned as is, and origType is 'noConversion'.
    @return a tuple with the unicodified string and the original string encoding.
    '''

    import unicodedata

def unicodify(st):
    # Verificar si la cadena es de tipo str (Unicode en Python 3)
    if isinstance(st, str):
        origType = 'str'
    elif isinstance(st, bytes):
        try:
            # Decodificar la cadena de bytes a Unicode utilizando utf-8
            st = st.decode('utf-8')
            origType = 'utf-8'
        except UnicodeDecodeError:
            try:
                # Si falla la decodificación utf-8, intentar decodificarla utilizando latin-1
                st = st.decode('latin1')
                origType = 'latin1'
            except:
                raise UnicodeEncodeError('Given string %s must be either Unicode, UTF-8 or Latin-1' % repr(st))
    else:
        origType = 'noConversion'

    # Normalizar el Unicode (para combinar cualquier caracter que se combine, por ejemplo, acentos, en la letra anterior)
    if origType != 'noConversion':
        st = unicodedata.normalize('NFKC', st)

    return st, origType


def deunicodify(unicodifiedStr, origType):
    '''
    Convert the given unicodified string back to its original type and encoding
    '''

    if origType == 'unicode':
        return unicodifiedStr
    
    # Si origType es 'str', simplemente devuelve la cadena sin codificarla nuevamente
    if origType == 'str':
        return unicodifiedStr

    return unicodifiedStr.encode(origType)