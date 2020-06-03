import { TestBed } from '@angular/core/testing';

import { EtuService } from './etu.service';

describe('EtuService', () => {
  let service: EtuService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EtuService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
