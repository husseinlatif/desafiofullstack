import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DesafioFullstackComponent } from './desafio-fullstack.component';

describe('DesafioFullstackComponent', () => {
  let component: DesafioFullstackComponent;
  let fixture: ComponentFixture<DesafioFullstackComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DesafioFullstackComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DesafioFullstackComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
