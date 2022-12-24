import '../styles/globals.css'

export default function App({ Component, pageProps }) {
  return (
    <div class="bg-blue-200">
      <Component {...pageProps} />
    </div>
  )
}
