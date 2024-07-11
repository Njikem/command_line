import dbhelpers  

#result = dbhelpers.run_statement('call get_post();')
#print(result)



#result_two = dbhelpers.run_statement('call get_client(?, ?)', ['Bright', 'Brity'])
#print(result_two)

#result_two = dbhelpers.run_statement('call get_client(?, ?)', ['Bright', 'Brity'])
#print(result_two)


def  login_client():
   
        
        username = input('What is your username?')
        password = input('What is your password?')
        print(username)
        print(password)

        result = dbhelpers.run_statement('call get_client(?, ?)', [username, password])
        print(result)

        if(result[0]['id'] ):
                return result[0]['id']
        
        else:
                return None
        

login_client()


#Function to create post
def create_post(client_id):

       
        title = input('Write the title')
        content = input('Write the content')
        print(title)
        print(content)
        results = ('create_post(?, ?, ?)', [client_id, title, content])
        print(results)
                           


create_post('client_id')



#function to get all the post

def get_post():
        results = dbhelpers.run_statement('call get_post()', [])
        for result in results:
                print(result)
    
        
get_post()


