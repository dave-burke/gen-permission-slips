import type { PermissionSlipData } from './permission-slip-form.types.ts'

export const defaultFormData: PermissionSlipData = {
  images: {
    header1: '',
    header2: '',
    header3: '',
  },
  dueDate: '',
  camp: {
    name: '',
    url: '',
    phone: '',
    address: '',
    site: '',
    type: 'tent camping',
    messkits: true,
    map: '',
  },
  cost: {
    scout: '',
    adult: '',
  },
  departure: {
    location: '',
    time: '',
  },
  return: {
    location: '',
    time: '',
  },
  troop: {
    number: '',
  },
  coordinator: {
    name: '',
    address: '',
    phone: '',
    email: '',
  },
}
