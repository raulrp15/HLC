describe('template spec', () => {
  it('uno', () => {
    cy.request('GET','raulcrudapi.azurewebsites.net/api/personaapi')
    .then((response) =>{
      expect(response.status).to.eq(200)
      cy.log(JSON.stringify(response.body));
    })
    
  })
  it('otro', () => {
    cy.request('GET','https://raulcrudapi.azurewebsites.net/api/departamentoapi/1')
    .then((response) =>{
      cy.log(JSON.stringify(response.body));
    })
  })

  it('post', () => {
    cy.request('POST','https://lorenzoasp.azurewebsites.net/api/personaapi',
      {
        "id": 0,
        "nombre": "Raul",
        "apellidos": "Lopez",
        "telefono": "123456789",
        "direccion": "Calle 123",
        "fechaNacimiento": "2023-05-01T00:00:00",
        "nombreDept": "Ventas",
        "idDepartamento": 1
      }
    )
    .then((response) =>{
      cy.log(JSON.stringify(response.body));
    })
  })
})