import {OnInit, AfterViewInit, Component, ViewChild} from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import {MatTableDataSource} from '@angular/material/table';
import { UserServiceService } from '../services/user-service.service'

@Component({
  selector: 'app-desafio-fullstack',
  templateUrl: './desafio-fullstack.component.html',
  styleUrls: ['./desafio-fullstack.component.css']
})
export class DesafioFullstackComponent implements AfterViewInit {

  constructor(private userService: UserServiceService ) {
    

   }

   
   usersData: DataElement[] = [
     {
     username: "ANPINA",
     email: "antonio.pina@tvglobo.com.br",
     inclusionDate: "28/05/2019",
     alterationDate: "30/05/2019",
     rule: "01",
     status: "ATIVO"
    },
    {
      username: "CCHANG",
      email: "ciro.chang@tvglobo.com.br",
      inclusionDate: "28/05/2019",
      alterationDate: "30/05/2019",
      rule: "01",
      status: "ATIVO"
     },
     {
      username: "TMARCAL",
      email: "thiago.marcal@tvglobo.com.br",
      inclusionDate: "28/05/2019",
      alterationDate: "30/05/2019",
      rule: "01",
      status: "ATIVO"
     },
     {
      username: "ECGIANN",
      email: "ecgianotto@tvglobo.com.br",
      inclusionDate: "28/05/2019",
      alterationDate: "30/05/2019",
      rule: "01",
      status: "ATIVO"
     },
     {
      username: "YFERNAND",
      email: "yuri.vasquez@tvglobo.com.br",
      inclusionDate: "28/05/2019",
      alterationDate: "30/05/2019",
      rule: "01",
      status: "ATIVO"
     },
     {
      username: "PLACERDA",
      email: "pedro.soares.lacerda@tvglobo.com.br",
      inclusionDate: "28/05/2019",
      alterationDate: "30/05/2019",
      rule: "01",
      status: "ATIVO"
     },
     {
      username: "ANPINA",
      email: "antonio.pina@tvglobo.com.br",
      inclusionDate: "28/05/2019",
      alterationDate: "30/05/2019",
      rule: "01",
      status: "ATIVO"
     },
     {
       username: "CCHANG",
       email: "ciro.chang@tvglobo.com.br",
       inclusionDate: "28/05/2019",
       alterationDate: "30/05/2019",
       rule: "01",
       status: "ATIVO"
      },
      {
       username: "TMARCAL",
       email: "thiago.marcal@tvglobo.com.br",
       inclusionDate: "28/05/2019",
       alterationDate: "30/05/2019",
       rule: "01",
       status: "ATIVO"
      },
      {
       username: "ECGIANN",
       email: "ecgianotto@tvglobo.com.br",
       inclusionDate: "28/05/2019",
       alterationDate: "30/05/2019",
       rule: "01",
       status: "ATIVO"
      },
      {
       username: "YFERNAND",
       email: "yuri.vasquez@tvglobo.com.br",
       inclusionDate: "28/05/2019",
       alterationDate: "30/05/2019",
       rule: "01",
       status: "ATIVO"
      },
      {
       username: "PLACERDA",
       email: "pedro.soares.lacerda@tvglobo.com.br",
       inclusionDate: "28/05/2019",
       alterationDate: "30/05/2019",
       rule: "01",
       status: "ATIVO"
      },
    ]
   
    @ViewChild(MatPaginator) paginator: MatPaginator;

   dataSource = new MatTableDataSource<any>(this.usersData);
   
   columnsToDisplay: string[] = ['user', 'email', 'inclusionDate', 'alterationDate', 'rules', 'status', 'actions'];
   
   

  displayOverlay:boolean = false
  openOverlay(){
    if (!this.displayOverlay){
      this.displayOverlay = true;
    }

  }

  ngAfterViewInit(): void {
    this.dataSource.paginator = this.paginator;
  }
}

export interface DataElement {
  username: string;
  email: string;
  inclusionDate: string,
  alterationDate: string,
  rule: string,
  status: string
}
