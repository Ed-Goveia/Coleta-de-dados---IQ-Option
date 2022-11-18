
r = 0
g = 0
g_a =0
r_a = 0
doji = 0
doji_lu =0
signal = None
r_p = 0
g_p = 0
g_t = 0
r_t = 0
r_q = 0
g_q = 0
r_y = 0
g_y = 0
g_one = 0
r_one = 0
r_last = 0
g_last = 0

if doji == 0:
    
    if doji_lu == 1:
        if r_a == 11: signal = 'put'
        if g_a == 11: signal = 'call'
        if r_a == 10: signal = 'put'
        if g_a == 10: signal = 'call'
        if r_a == 9 : signal = 'put'
        if g_a == 9 : signal = 'call'
    
    if doji_lu == 0:
        if r_a == 11: signal = 'call'
        if g_a == 11: signal = 'put'
        if r_a == 10: signal = 'put'
        if g_a == 10: signal = 'call'
        if r_a == 9 : signal = 'call'
        if g_a == 9 : signal = 'put'
        
        elif g_a < 9 and r_a < 9:
            if r < 5 and g < 5:
                if g_a < 9 and r_a < 9:
                    
                    # Padrão - # G R R R R --- reformulado
                    
                    if r_q == 4: 

                        if r_p == g_p: signal = 'call'
                            
                        if g_a < 9 and r_a < 9:
                            if r_p != g_p:
                                if r_a < 9 and r_y < g_y and r_a > g_a : signal = 'put'
                                if g_a < 10 and g_y < r_y and g_a > r_a or r_a >= 9: signal = 'call'
                                if r_y == g_y:
                                    if g_p < r_p : signal = 'call'
                                    if r_p < g_p: signal = 'put'
                                 
                    # Padrão - R G G G G --- reformulado
                    if g_q == 4: 

                        if r_p == g_p: signal = 'put'
                  
                        if g_a < 10 and r_a < 10:
                            if r_p != g_p:
                                if r_a < 10 and r_y < g_y and r_a > g_a or g_a >= 9: signal = 'put'
                                if g_a < 9 and g_y < r_y and g_a > r_a : signal = 'call'
                                if r_y == g_y:
                                    if g_p < r_p : signal = 'call'
                                    if r_p < g_p: signal = 'put'
                            
                    if g_q < 4:
                        
                        # Padrões de inversão
                        
                        if g_q == 3 and g_t == 3:   
                            
                            # Padrão - R R G G G --- inversão para minoria (saturada)
                            if g == 3:
                                if r_a == g_a: signal = 'put'
                                
                                if r_a - 1 == g_a or g_a - 1 == r_a: 
                                    if g_p - 1 > r_p :signal = 'call'
                                    elif r_p - 1 > g_p: signal = 'put'
                                    else: signal = signal = 'put'
                                
                                if r_a - 1 > g_a or g_a - 1 > r_a:
                                    if doji_lu == 0:
                                        if r_a < 10 and g_a < 10:
                                            if r_p < 9 and g_p < 9: 
                                                if g_p - 1 > r_p: signal = 'call'
                                                if r_p - 1 > g_p : signal = 'put'
                                                else: signal = 'put'
                                            
                            # Padrão - G R G G G --- força
                            if g == 4 and r_q == 1: 
                                
                                if doji_lu == 1:
                                    if r_y == g_y: signal = 'put'
                                    
                                if g_a == r_a: signal = 'put'
                                if r_p == g_p: signal = 'put'
                                if r_a != g_a:
                                    if r_p != g_p:
                                        if g_p < 9 and r_p < 9: 
                                            if g_a < 9: signal = 'call'
                                            if g_a == 9: signal = 'put'
                                        
                        # Padrões de G

                        if r_a < 11 and g_a < 11 :
                            if g_t < 3:
                            
                                # Padrões de força
                                # Respectivamente - G G G G R , G G R G G --- Comprimido
                                if g == 4:
                                    if r_one == 1: 
                                        
                                        if r_p == g_p: signal = 'put'
                                        
                                        if r_a < 9 and g_a < 9:
                                            if r_p == g_p: signal = 'call'
                                            if r_p < 9 and g_p < 9: 
                                                if r_p - 1 == g_p: signal = 'call'
                                                if r_p - 1 > g_p: signal = 'put'
                                                if g_p > r_p: signal = 'call'
                                    
                                    if r_t == 1 and g_last ==2: 
                                                                    
                                        if r_a < 9 and g_a < 9:
                                            if r_p == g_p: signal = 'call'
                                            if r_p != g_p:
                                                if g_p < 9 and r_p < 9: 
                                                    if g_p > r_p: signal = 'call'
                                                    if r_p - 1 == g_p : signal = 'call'
                                                    if r_p - 1 > g_p: signal = 'put'
                                                
                                            
                                # Padrão - G G G R G --- reduzido
                                    if g_q == 3 and r_last == 1 and g_one == 1: 
                                
                                        if r_p == g_p: signal = 'put'
                                        if r_a == g_a: signal = 'put'
                                        
                                        if r_a - 1 == g_a or g_a - 1 == r_a: signal = 'call'
                                        if r_a - 1 > g_a or g_a - 1 > r_a:
                                            if doji_lu == 0:
                                                if r_a != g_a:
                                                    if g_a < 9 and r_a < 9:
                                                        if r_p != g_p:
                                                            if g_p < 9 and r_p < 9:
                                                                if g_p > r_p : signal = 'call'
                                                                if r_p > g_p : signal = 'put'   
                    if r_q < 4:
                        
                        if r_q == 3 and r_t == 3:     
                            
                            # Padrão - G G R R R --- Padrão melhorado

                            if r == 3: 
                                if r_a == g_a: signal = 'call'
                                
                                if r_a - 1 == g_a or g_a - 1 == r_a: 
                                    if r_p - 1 > g_p: signal = 'put'
                                    elif g_p - 1 > r_p :signal = 'call'
                                    else: signal = signal = 'call'
                                
                                if r_a - 1 > g_a or g_a - 1 > r_a:
                                    if doji_lu == 0:
                                        
                                        if g_a < 10 and r_a < 10:
                                            if r_p < 9 and g_p < 9:
                                                if r_p - 1 > g_p: signal = 'put'
                                                if g_p - 1 > r_p: signal = 'call'
                                                else: signal = 'call'
                                            
                            
                            # Padrâo - R G R R R --- força
                            
                            if r == 4:

                                if g_q == 1: 
                                    if doji_lu == 1:
                                        if r_y == g_y: signal = 'call'
                                
                                    if g_a == r_a: signal = 'call'
                                    if r_p == g_p: signal = 'call'
                                    if r_a != g_a:
                                        if r_p != g_p:
                                            if g_p < 9 and r_p < 9: 
                                                if r_a < 9: signal = 'put'
                                                if r_a == 9: signal = 'call'
                                                
        
                        if r_a < 11 and g_a < 11:
                            if r_t < 3:
                            
                                #Padrões de força:
                                # Padrões, respectivamente, R R R R G, R R G R R --- Comprimido
                                if r == 4:
                                    if g_one == 1: 
                                        
                                        if r_p == g_p: signal = 'call'
                        
                                        if r_a < 9 and g_a < 9:
                                            if r_p < 9 and g_p < 9: 
                                                if g_p - 1 == r_p: signal = 'put'
                                                if g_p - 1 > r_p: signal = 'call'
                                                if r_p > g_p: signal = 'put'


                                # Padrão R R G R R
                                    if g_t == 1 and r_last == 2:                                                                   
                                        
                                        if r_a < 9 and g_a < 9:
                                            if r_p == g_p: signal = 'put'
                                            if r_p != g_p:
                                                if g_p < 9 and r_p < 9: 
                                                    if r_p > g_p:signal = 'put'
                                                    if g_p - 1 == r_p : signal = 'put'
                                                    if g_p - 1 > r_p: signal = 'call'        

                                # Padrão - R R R G R --- força
                                    if g_last == 1 and r_one == 1:
                                        
                                        if r_p == g_p: signal = 'call'
                                        if r_a == g_a: signal = 'call'
                                        
                                        if r_a - 1 == g_a or g_a - 1 == r_a: signal = 'put'
                                        
                                        if r_a - 1 > g_a or g_a - 1 >  r_a:
                                            if doji_lu == 0:
                                                if r_a != g_a:
                                                    if g_a < 9 and r_a < 9:
                                                        if r_p != g_p:
                                                            if g_p < 9 and r_p < 9:
                                                                if g_p > r_p : signal = 'call'
                                                                if r_p > g_p : signal = 'put'
                                                                                                          
                if r_q < 4 and g_q < 4:
                    
                    if g_t < 3 and r_t < 3:

                        if r_a == g_a: 
                            if r > g: signal = 'call'
                            if g > r: signal = 'put'
                        if r_a - 1 == g_a or g_a - 1 == g_a: 
                            if r_p - 1 > g_p: signal = 'put'
                            elif g_p - 1 > r_p: signal = 'call'
                            else: 
                                if r > g: signal = 'call'
                                if g > r: signal = 'put'
        
            