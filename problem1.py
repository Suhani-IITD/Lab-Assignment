import numpy as np

def win_factory(w, h, p): 
   def win(Img, i, j): # returns w*h list of floats, around I[i,j], padded with p if required
      ans = []
      rmax,cmax = Img.shape[0],Img.shape[1]
      for r in range((-1)*(h//2) , (h//2)+1):
         for c in range((-1)*(w//2) , (w//2)+1):
            row,col = i+r , j+c
            if(row<0 or row>=rmax or col<0 or col>=cmax):
               ans.append(p)
            else:
               ans.append(Img[row][col])
      return ans
               
   return win

def filter1_factory(table, transform): 
   def filter1(gv_list):# Use reduction.
      new = np.array(transform(gv_list))
      t = np.array(table)
      return np.dot(new,t)
      
      
      
   
   return filter1

def filter_image_array(ImgArr, f): 
   I2 = np.empty(ImgArr.shape)
   ## Write you code here
   for i in range(ImgArr.shape[0]):
      for j in range(ImgArr.shape[1]):
         val = f(ImgArr,i,j)
         I2[i][j] = val
   
   ## Your code ends here
   return I2
   
# do not change make_filter function. We have already written it for you.
# Understand what it does. 
def make_filter(pass1f, pass2f):
      def filterij(ImgArr, row, col):
         return pass2f(pass1f(ImgArr, row, col))
      return filterij


# do not change the blur function. We have already written it. 
# Understand what it does. 
def problem1():
    def blur(ImgArr): 
       def transform(flist):
          return flist # No transform
       winf = win_factory(3, 3, 0) # 3x3 wide window
       filterf = filter1_factory([1.0/9 for i in range(9)], transform) # Average
       return filter_image_array(ImgArr, make_filter(winf, filterf))
       
    # You are also provided the implementation for maxpool, 
    # look at it to see how the maxpool filter is implemented 
    
    
    def maxpool(ImgArr):
       def transform(flist):
          return [max(flist)]
       winf = win_factory(5, 5, 0) # 5x5 wide window
       filterf = filter1_factory([1], transform)
    
       return filter_image_array(ImgArr, make_filter(winf, filterf))
    def ridge(ImgArr):
       def transform(flist):
          return flist
       winf = win_factory(3, 3, 0)
       k = [-1,-1,-1,-1,8,-1,-1,-1,-1]
       filterf = filter1_factory(k, transform) # Average
       return filter_image_array(ImgArr, make_filter(winf, filterf))
       
        
    return blur, ridge






