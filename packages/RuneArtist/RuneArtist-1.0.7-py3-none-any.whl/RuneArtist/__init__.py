from matplotlib import pyplot as plt
import os, io
import PIL

class RuneArtist():
    def __init__(self):
        self.current_path = os.path.dirname(os.path.abspath(__file__))
        self.pictures_dir = '/pictures/'

        self.pictures = {
            picture.split('.')[0]: PIL.Image.open(self.current_path + self.pictures_dir + picture)
            for picture in os.listdir(self.current_path + self.pictures_dir)
        }
    
    def draw(self, message, return_type='fig'):
        max_height = max([i.size[0] for i in self.pictures.values()])
        X_start_max = 0

        fig = plt.figure()
        fig.canvas.manager.set_window_title('Runes')

        X_start, y_start = 0, max_height*(len(message) - 1)
        for row in message:
            for char in row:
                fig.figimage(self.pictures[char], X_start, y_start)
                X_start += self.pictures[char].size[0] * 1.1
            
            if X_start > X_start_max:
                X_start_max = X_start
                
            y_start -= max_height
            X_start = 0
        
        fig.set_size_inches(X_start_max / 100, max_height * (len(message)) / 100)
        fig.tight_layout()
        
        match return_type:
            case 'fig':
                return fig
            case 'pil':
                buf = io.BytesIO()
                fig.savefig(buf)
                buf.seek(0)
                return PIL.Image.open(buf)
                 
