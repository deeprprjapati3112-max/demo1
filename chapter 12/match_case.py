def deep_status (status):
    match status:
        
        case 200:
            return "ok"
        
        case 404:
            return "not found"
        
        case 500:
            return"internal server error"
        
        case _:
            return"unknow status"
             
print(deep_status(500))    
print(deep_status(8789))         
            
            
                