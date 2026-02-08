//typscript structure with zustand
import { create } from 'zustand'

interface UserLoginModalState {
  open: boolean
  openModal: () => void
  closeModal: () => void
}

const useUserLoginModal = create<UserLoginModalState>((set) => ({
  open: false,
  openModal: () => set({ open: true }),
  closeModal: () => set({ open: false }),
}))

export default useUserLoginModal


//JavaScript with zustand(NO interface)

import { create } from 'zustand'

const useUserLoginModal = create((set) => ({
  open: false,
  openModal: () => set({ open: true }),
  closeModal: () => set({ open: false }),
}))

export default useUserLoginModal


