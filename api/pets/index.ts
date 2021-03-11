/* eslint-disable */
export type Methods = {
  get: {
    query?: {
      limit?: number
    }

    status: 200
    resBody: {
      id: number
      name: string
      tag?: string
    }[]

    resHeaders: {
      'x-next': string
    }
  }
}
