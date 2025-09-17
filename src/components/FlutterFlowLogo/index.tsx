import React from "react";
import { useThemeConfig, useColorMode } from '@docusaurus/theme-common';
import styles from './index.module.css';


const FlutterFlowLogo = () => {
    const logoSrcDark = "/logos/DreamFlow-Logo-Black.png"; // Light mode logo
    const logoSrcLight = "/logos/DreamFlow-Logo.png"; // Dark mode logo
    const { colorMode } = useColorMode();

    return (
        <div className={styles.container}>
            <img
                src={colorMode === 'dark' ? logoSrcDark : logoSrcLight}
                alt={`Dreamflow Logo`}
                className={styles.logo}
            />
        </div>
    );
};

export default FlutterFlowLogo;
