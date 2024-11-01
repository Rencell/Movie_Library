import http from "./http-header/multi";
import https from "./http-header/application";

class movieService{
    
    getAll(){
        return http.get('/movie');
    }
    create(form){
        return http.post('/movie/', form);
    }
    show(id){
        return http.get(`/movie/${id}/`);
    }
    partial(id, form){
        return http.patch(`/movie/${id}/`, form);
    }
    update(id, form){
        return http.put(`/movie/${id}/`, form);
    }
    destroy(id){
        return http.delete(`/movie/${id}/`);
    }
    
}

export default new movieService();