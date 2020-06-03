import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { EtuService } from '../services/etu.service';


@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.scss']
})
export class ListComponent implements OnInit {

  listeEtu : any[];

  constructor(private etuService: EtuService) { }

  ngOnInit(): void {
    this.etuService.listSubject.subscribe(
      (val: any[]) => {
        this.listeEtu = val;
      }
    );

    this.etuService.get();

  }

}
