import React from 'react'
import { Text, Link, HStack, Center, Heading, Switch, useColorMode, NativeBaseProvider, extendTheme, VStack, Code } from 'native-base'
import NativeBaseIcon from './components/NativeBaseIcon'
import { NavigationContainer } from '@react-navigation/native'
import { createDrawerNavigator } from '@react-navigation/drawer'

import Home from './screens/Home'

// Define the config
const config = {
  useSystemColorMode: false,
  initialColorMode: 'dark',
}

// extend the theme
export const theme = extendTheme({ config })

const Drawer = createDrawerNavigator()

export default function App() {
  return (
    <NavigationContainer>
      <Drawer.Navigator>
        <Drawer.Screen
          name='Home'
          component={Home}
          options={{
            drawerLabel: 'Home',
          }}
        />
      </Drawer.Navigator>
    </NavigationContainer>
  )
}

// Color Switch Component
function ToggleDarkMode() {
  const { colorMode, toggleColorMode } = useColorMode()
  return (
    <HStack space={2} alignItems='center'>
      <Text>Dark</Text>
      <Switch isChecked={colorMode === 'light' ? true : false} onToggle={toggleColorMode} aria-label={colorMode === 'light' ? 'switch to dark mode' : 'switch to light mode'} />
      <Text>Light</Text>
    </HStack>
  )
}
