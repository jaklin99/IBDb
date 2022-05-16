import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'
import Header from '../components/header';
import Footer from '../components/footer';
import HomePage from '../pages/home';


export default function Home() {
  return (
    <div>
      <Header/>
      <HomePage/>
      <Footer/>
    </div>
  )
}
