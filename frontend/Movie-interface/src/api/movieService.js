import http from "./index";

class movieService{
    
    getAll(){
        return http.get('/movie');
    }
    create(form){
        return http.post('/movie/', form);
    }
    destroy(id){
        return http.delete(`/movie/${id}/`);
    }
    
}

export default new movieService();