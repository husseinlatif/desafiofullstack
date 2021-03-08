import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs'



@Injectable({
  providedIn: 'root'
})
export class UserServiceService {

  constructor(private http: HttpClient) { }

  apiURL = 'http://localhost:3333/users/'
  
  httpHeaders: object = {
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
    }
  }

  

  createUser = (body):Observable<any> => {
    return this.http.post(this.apiURL, JSON.stringify(body), this.httpHeaders)
  }

  listAllUsers = ():Observable<any> => {
    return this.http.get(this.apiURL, this.httpHeaders)
  }

  listUser = (id:string):Observable<any> => {
    return this.http.get(this.apiURL + id, this.httpHeaders)
  }

  editUser = (id:string, body):Observable<any> => {
    return this.http.put(this.apiURL + id, JSON.stringify(body), this.httpHeaders)
  }

  deleteUser = (id:string):Observable<any> => {
    return this.http.delete(this.apiURL + id, this.httpHeaders)
  }
}
