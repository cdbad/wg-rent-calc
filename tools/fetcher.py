from tkinter import ttk

class Fetcher:
    def fetch_data(self, frame: ttk.Frame) -> dict:
        # title frame
        data = dict()
        data['Name'] = frame\
            .children['!frame']\
            .children['!label']\
            .cget('text')
        
        # main frame
        i = 0
        main_frame = list(
            frame\
            .children['!frame2']\
            .children\
            .values()
        )
        while i < len(main_frame):
            if str(main_frame[i + 1]['foreground']) == 'grey':
                data[main_frame[i].cget('text')] = ''
            else:
                data[main_frame[i].cget('text')] = main_frame[i + 1].get()
            i += 2
        
        # room frame
        room_frames = frame.children['!frame4'].children
        room_frames_keys = room_frames.keys()
        rooms = [room_frames[key].children for key in room_frames_keys]
        
        for room in rooms:
            room_name = room['!label'].cget('text')

            data[room_name] = dict()
            
            if str(room['!entry']['foreground']) == 'grey':
                data\
                [room_name]\
                [room['!label3'].cget('text')] = ''
            else:
                data\
                [room_name]\
                [room['!label3'].cget('text')] = room['!entry'].get()
            
            if str(room['!entry2']['foreground']) == 'grey':
                data\
                [room_name]\
                [room['!label4'].cget('text')] = ''
            else:
                data\
                [room_name]\
                [room['!label4'].cget('text')] = room['!entry2'].get()
        
        return data