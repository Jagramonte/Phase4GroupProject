import React, { useState } from 'react';
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import 'react-tabs/style/react-tabs.css'; // Import the styles
import './App.css'; // Create this file for your own styles

const App = () => {
  const [tabIndex, setTabIndex] = useState(0);

  const handleTabSelect = (index) => {
    setTabIndex(index);
  };

  return (
    <div>
      <Tabs selectedIndex={tabIndex} onSelect={handleTabSelect}>
        <TabList>
          <Tab>my Favs</Tab>
          <Tab>Horror</Tab>
          <Tab>Action</Tab>
          <Tab>Romance</Tab>
          <Tab>Sci-Fi</Tab>
          <Tab>Comedy</Tab>
        </TabList>

        <TabPanel>
          {/* Content for Tab 1 */}
          <p>Content for Tab 1</p>
        </TabPanel>
        <TabPanel>
          {/* Content for Tab 2 */}
          <p>Content for Tab 2</p>
        </TabPanel>
        <TabPanel>
          {/* Content for Tab 3 */}
          <p>Content for Tab 3</p>
        </TabPanel>
        <TabPanel>
          {/* Content for Tab 4 */}
          <p>Content for Tab 4</p>
        </TabPanel>
        <TabPanel>
          {/* Content for Tab 5 */}
          <p>Content for Tab 5</p>
        </TabPanel>
        <TabPanel>
          {/* Content for Tab 6 */}
          <p>Content for Tab 6</p>
        </TabPanel>
      </Tabs>
    </div>
  );
};

export default App;
