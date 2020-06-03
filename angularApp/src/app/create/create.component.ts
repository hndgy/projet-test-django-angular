import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { EtuService } from '../services/etu.service';

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.scss']
})
export class CreateComponent implements OnInit {


 

  createForm : FormGroup;


  constructor(private formBuilder: FormBuilder, private http: HttpClient, private etuService: EtuService) { }

  ngOnInit(): void {
    this.initForm();
  }

  onSubmit(){
    
    console.log("submit ");
    
    const num = this.createForm.get('num').value;
    const nom = this.createForm.get('nom').value;
    const prenom = this.createForm.get('prenom').value;

    this.http.post("http://127.0.0.1:8000/api/etu/", {"num" : num, "nom": nom, "prenom": prenom}).subscribe(res => {
        this.etuService.get();
    });

  


  }

  initForm(){
    
    this.createForm = this.formBuilder.group({
      num : ['',[Validators.required]],
      nom : ['',[Validators.required]],
      prenom : ['',[Validators.required]]
    });

  }


}
