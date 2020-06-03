import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class EtuService {
  
  list: any[];
  listSubject = new Subject(); 

  emit(){
    this.listSubject.next(this.list);
  }

  constructor(private http: HttpClient) { }





  ngOnInit(): void {

    
    
  }


  get(){
    this.http.get("http://localhost:8000/api/etu").subscribe(
      (list: any[]) => {
        this.list = list;
        this.emit();
      }
    );

  }


}
