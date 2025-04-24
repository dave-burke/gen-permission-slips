export interface PermissionSlipData {
  images: {
    header1: string
    header2: string
    header3: string
  }
  dueDate: string
  camp: {
    name: string
    url: string
    phone: string
    address: string
    site: string
    type: string // e.g. 'tent camping'
    messkits: boolean
    map: string
  }
  cost: {
    scout: string
    adult: string
  }
  departure: {
    location: string
    time: string
  }
  return: {
    location: string
    time: string
  }
  troop: {
    number: string
  }
  coordinator: {
    name: string
    address: string
    phone: string
    email: string
  }
}
